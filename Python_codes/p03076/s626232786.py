import math

a = [int(input()) for _ in range(5)]
a_2 = [(i-1)%10 for i in a]

last_item=a[a_2.index(min(a_2))]
print(int(sum([math.ceil(i/10)*10 for i in a])+((last_item-1)%10-9)))
