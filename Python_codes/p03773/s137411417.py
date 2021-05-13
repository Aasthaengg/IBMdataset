#入力
lst = input().split()

time = int(lst[0]) + int(lst[1])

if 24 <= time:
   time = time - 24

#出力
print(time)