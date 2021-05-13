n=input()
l = list(map(int, input().split()))
print(" ".join(map(str, l[::-1])))