N,C = map(int,input().split())
stc = sorted([list(map(int,input().split())) for i in range(N)], key = lambda x:(x[2],x[0]))
cnow = 0
tnow = 0
end = max(i[1] for i in stc)
imos = [0 for i in range(end+2)]
for s,t,c in stc:
    if cnow == c and tnow == s:
        imos[s]+=1
    else:
        imos[s-1] += 1
    imos[t] -=1
    cnow = c
    tnow = t
for i in range(end):
    imos[i+1] += imos[i]
print(max(imos))