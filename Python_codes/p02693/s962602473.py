K = int(input())
A,B = map(int,input().split())

if K == 1:
    print("OK")
elif A%K == 0:
    print("OK")
elif A//K != B//K:
    print("OK")
else:
    print("NG")