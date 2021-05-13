n = int(input())
ll = []
wa = 0
for i in range(n):
    a,b = map(int, input().split())
    wa += b-a + 1
print(wa)