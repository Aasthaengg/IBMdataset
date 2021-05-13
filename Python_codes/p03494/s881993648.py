input()
def a(n):
    return 0 if n%2 else a(n//2)+1
print(min([a(i) for i in list(map(int,input().split()))]))