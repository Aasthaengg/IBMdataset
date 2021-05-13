N = int(input())
st = list(set(map(int,input().split())))
total = 0
st.sort()

for i in range(len(st)-1):
    total += (abs(st[i]-st[i+1]))
print(total)