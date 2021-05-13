n = input()
while n != "0":
    ans = 0
    for i in range(len(n)):
        ans += ord(n[i:i+1]) - 48

    print(ans)
    n = input()