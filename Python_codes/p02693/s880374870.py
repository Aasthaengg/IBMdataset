K = int(input())
A, B=map(int, input().split())
li = [i for i in range(A, B+1)]
if any(i%K == 0 for i in li):
    print("OK")
else:
    print("NG")