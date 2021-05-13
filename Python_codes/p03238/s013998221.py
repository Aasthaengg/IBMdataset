#ABC-112-A
N = int(input())
if N == 1:
    print("Hello World")
else:
    ans = 0
    for _ in range(2):
        AB = int(input())
        ans += AB
    print(ans)