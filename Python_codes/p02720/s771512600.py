k=int(input())
cnt=0
queue=['1','2','3','4','5','6','7','8','9']
while len(queue)>0:
  if cnt==k:
    print(queue[-1][:-1])
    exit()
  now=queue.pop(0)
  if now[-1]=='9':
    queue.append(now+'8')
    queue.append(now+'9')
  elif now[-1]=='0':
    queue.append(now+'0')
    queue.append(now+'1')
  else:
    queue.append(now+str(int(now[-1])-1))
    queue.append(now+str(int(now[-1])))
    queue.append(now+str(int(now[-1])+1))
  cnt+=1