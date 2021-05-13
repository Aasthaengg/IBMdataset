a, b = map(int, input().split())
for p in range(b*10, b*10+10):
    if int(p*0.08) == a:
        print(p)
        break
else:
    print(-1)