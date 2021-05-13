a,b,c,d=list(input())
a,b,c,d=int(a),int(b),int(c),int(d)
op=["+","-"]
for i in range(2):
  for j in range(2):
    for k in range(2):
      if i == 0:
        if j == 0:
          if k == 0:
            ans = a+b+c+d
          else:
            ans = a+b+c-d
        else:
          if k == 0:
            ans = a+b-c+d
          else:
            ans = a+b-c-d
      else:
        if j == 0:
          if k == 0:
            ans = a-b+c+d
          else:
            ans = a-b+c-d
        else:
          if k == 0:
            ans = a-b-c+d
          else:
            ans = a-b-c-d
      if ans == 7:
        print(str(a)+op[i]+str(b)+op[j]+str(c)+op[k]+str(d)+"=7")
        quit()