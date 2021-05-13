s = int(input())
dict = {s:1}
while(1):
    if s % 2 == 0:
        s = s // 2
    else:
        s = 3 * s + 1
    if s in dict:
        break
    else:
        dict[s] = 1
print(len(dict)+1)