abcd = input()

l = ["+", "-"]
for i in l:
  for j in l:
    for k in l:
      ans = eval(abcd[0]+i+abcd[1]+j+abcd[2]+k+abcd[3])
      if ans == 7:
        print(abcd[0]+i+abcd[1]+j+abcd[2]+k+abcd[3]+"=7")
        exit()