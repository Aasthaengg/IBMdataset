a = input()
hl = int(len(a)/2)
first = a[:hl]
last = a[:hl+(len(a)%2-1):-1]
ans = 0
# print(first)
# print(last)
for fi,la in zip(first,last):
    if fi != la :
        ans += 1
print(ans)