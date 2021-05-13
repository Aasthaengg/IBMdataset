N = int(input())
aaa = [int(input()) for i in range(N)]
if all([a%2==0 for a in aaa]):
    print("second")
else:
    print("first")