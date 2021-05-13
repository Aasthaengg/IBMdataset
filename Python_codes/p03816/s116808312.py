# solution
import io
data = int(input())
array = list(map(int, input().split()))
strings = len(set(array))
if data % 2 == strings % 2:
    print(strings)
else:
    print(strings - 1)