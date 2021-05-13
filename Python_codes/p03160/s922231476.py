import sys

n = int(sys.stdin.readline())
numbers = sys.stdin.readline().split()
for i in range(n):
    numbers[i] = int(numbers[i])
a_list = [0, abs(numbers[1] - numbers[0])]
if n > 2:
    a_list.append(abs(numbers[2] - numbers[0]))
else:
    print(a_list[-1])
    sys.exit()
for i in range(3, n):
    a_list.append(min(a_list[i-1]+abs(numbers[i-1] - numbers[i]), a_list[i-2]+abs(numbers[i-2] - numbers[i])))
print(a_list[-1])
sys.exit()