s = input()
length = len(s)
idx = 0
list = []
def func(x) :
    return abs(x-753)
while idx + 3 <= length  :
    list.append(int(s[idx:idx+3]))
    idx += 1
print(min(map(func, list)))
