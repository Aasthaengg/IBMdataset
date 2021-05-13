h, w = map(int, input().split())

w1 = ['#']*(w+2)

ans = []
ans.append(w1)

for i in range(h):
    tmp = ["#"]+list(input())+["#"]
    ans.append(tmp)

ans.append(w1)

for j in ans:
    for k in j:
        print(k, end="")
    print()