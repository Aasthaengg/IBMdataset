n = int(input())
l = list(map(int,input().split()))
a = set(l)
print(len(a) if (len(l)-len(a))%2 == 0 else len(a)-1)