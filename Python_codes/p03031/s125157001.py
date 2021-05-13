n, m = map(int, input().split())

switch_list = []

for i in range(m):
    s  = list(map(int, input().split()))
    s.pop(0)
    switch_list.append(s)
p_list = list(map(int, input().split()))
#print(switch_list)
#print(p_list)

ans = 0

for bit in range(1 << n): #100・・0(n+1桁)-1 =　111・・・1(n桁)となりn桁のビット演算をfor文で回す
    cnt = 0
    for j in range(0,m):
        switch_sum = 0
        for i in range(n):
            if (bit >> i) & 1 and i+1 in switch_list[j]:
                switch_sum += 1
        if switch_sum%2 == p_list[j]:
            cnt += 1
            if cnt == m:
                ans += 1

print(ans)