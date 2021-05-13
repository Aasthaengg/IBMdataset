N = int(input())
al = list(map(int, input().split()))

rusekiwa = [al[0]]

for i in range(1,N):
    rusekiwa.append(rusekiwa[-1] + al[i])

#print(rusekiwa)
lst = []
for n in range(0,N-1):
    x = rusekiwa[n]
    y = rusekiwa[-1] - rusekiwa[n]
    lst.append(abs(x - y))
#print(lst)
print(min(lst))