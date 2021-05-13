import bisect

N= int(input())
a = map(int, input().split(" "))
b = map(int, input().split(" "))
c = map(int, input().split(" "))

a = sorted(a)
b = sorted(b)
c = sorted(c)

result = 0
for i in b:
    ta = bisect.bisect_left(a,i)
    tc = bisect.bisect_right(c,i)
    result += ta*(N-tc)
print(result)