H, A = map(int, input().split())
Ans = 0
while True:
    H -= A
    Ans += 1
    if H <= 0:
        break
print(Ans)