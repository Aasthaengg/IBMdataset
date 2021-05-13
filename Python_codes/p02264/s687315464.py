s=input()
d=s.split()
n=int(d[0])
q=int(d[1])
end_t=0
processes=[]
for i in range(n):
    processes.append([])
    s=input()
    d=s.split()
    processes[i].append(d[0])
    processes[i].append(int(d[1]))

cnt=0
i=0
while True:
    if processes[0][1]<=q:
       end_t+=processes[0][1]
       print(processes[0][0],end_t)
       processes.pop(0)
       cnt+=1
       if cnt==n:
           break
   
    else:
       processes[0][1]-=q
       end_t+=q
       processes.append(processes[0])
       processes.pop(0)
       i+=1

