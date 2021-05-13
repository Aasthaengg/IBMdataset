# A = [list(map(int, input().split())) for _ in range(3)]
# k = int(input())
# B = [int(input()) for _ in range(n)]
# X = list(map(int, input().split()))
# a, b, c = map(int, input().split())
S = input()
n = len(S)
judge = True
if n % 2 != 0:
    print("No")
    exit()
for i in range(0, n, 2):
    if S[i] != "h" or S[i+1] != "i":
        judge = False
print("Yes") if judge else print("No")
