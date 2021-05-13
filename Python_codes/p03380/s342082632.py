n=int(input())

t = list(map(int,input().split()))

t.sort()

max_value = t[-1]

mid_value = 0

for a in t:
    if abs(max_value/2-a) < abs(max_value/2-mid_value):
        mid_value = a

print(max_value, mid_value)