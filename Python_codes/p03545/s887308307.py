op=["+","-"]
a,b,c,d=map(str,input())

for o1 in op:
  for o2 in op:
    for o3 in op:
      form= a+o1+b+o2+c+o3+d
      if eval(form)==7:
        print(form+"=7")
        exit()