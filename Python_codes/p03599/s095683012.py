A, B, C, D, E, F = map(int,input().split())
answer_number = [0,0,0,0]
answer_max = 0
for i in range((F//(100*A))+1):
  for j in range(((F-100*A*i)//(100*B))+1):
    if i==0 and j ==0: continue
    for k in range(((F-100*A*i-100*B*j)//C)+1):
      for l in range(((F-100*A*i-100*B*j-C*k)//D)+1):
        if (C*k+D*l)/(A*i+B*j) <= E:
          if (C*k+D*l)/(A*i+B*j) > answer_max:
            answer_max = (C*k+D*l)/(A*i+B*j)      #### k
            answer_number = [i,j,k,l]
if answer_max == 0: print(100*A,0)
else:
  print(C*answer_number[2]+D*answer_number[3]+100*(A*answer_number[0]+B*answer_number[1]), C*answer_number[2]+D*answer_number[3])
  
