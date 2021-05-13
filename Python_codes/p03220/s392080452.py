n = int(input())
t, a = map(int, input().split())
lists = list(map(int, input().split()))

tmp_lists = [(t - i*0.006) for i in lists]
diff_lists = []
for i in tmp_lists:
  diff_lists.append(a-i if (a-i) >=0 else (a-i)* -1)
copy = diff_lists.copy()
copy.sort()
index = diff_lists.index(copy[0])
print(index+1)