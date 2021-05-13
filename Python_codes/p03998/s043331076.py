a,b,c=[list(input())[::-1]for i in [0,0,0]]
now=0
dic={"abc"[i]:i for i in range(3)}
while [a,b,c][now]:
    now=dic[[a,b,c][now].pop()]
print("ABC"[now])