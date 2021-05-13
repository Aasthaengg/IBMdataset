fn = []
for i in range(5):
  num = int(input())
  fn.append(int(num))

fcn = []   
for f in fn:
  if f%10 != 0:
    fcn.append([f,f%10-10])
  else :
    fcn.append([f,0])

fcn.sort(key=lambda x: x[1],reverse=True)    

sum = 0
for i in range(len(fcn)):
  if i != len(fcn)-1:
    sum += fcn[i][0] - fcn[i][1]
  else :
    sum += fcn[i][0]
  
print(sum)
