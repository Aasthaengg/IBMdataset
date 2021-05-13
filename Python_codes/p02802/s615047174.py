N,M = map(int,input().split())
#if 'AC':{1:-1}
#if 'WA'*2:{1:2}
problems = {}
correct = 0
penalty = 0
for i in range(M):
    p,s = map(str,input().split())
    p = int(p)
   
    if p not in problems.keys():
        if s == 'AC':
            problems[p] = -1
            correct += 1
        else: #if s == 'WA' and not ACed yet 
            problems[p] = 1
    else: 
        if s == 'AC' and problems[p] != -1: #first AC
            penalty += problems[p]
            problems[p] = -1
            correct += 1
        elif s == 'WA' and problems[p] != -1:
            problems[p] += 1
            
print(correct,penalty)