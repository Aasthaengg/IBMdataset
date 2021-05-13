N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
  
already = [0] * N
A = [-float("inf")] * N

for i in range(N):#スタート地点
  if already[i] == 0:
    already[i] = 1
    q = [i + 1]
    now = i + 1
    score = []
    T = True
    while T:
      now = P[now - 1]
      score.append(C[now - 1])
      if now in q:
        T = False
      else:
        q.append(now)
        already[now - 1] = 1
    
    #A.append(q)
    #S.append(score)
    #print(q)#ループのルート
    #print(score)#ループ中のスコア
    roop = sum(score)
    if len(q) >= K:
      aa = -float("inf")
      for j in range(len(q)):
        time = 0
        bb = 0
        p = j
        while time != K:
          time += 1
          bb += score[p]
          aa = max(aa, bb)
          p += 1
          if p == len(q):
            p = 0
      A[i] = aa      
    else:  
      if roop <= 0:
        aa = -float("inf")
        for j in range(len(q)):
          time = 0
          bb = 0
          p = j
          while time != len(q):
            time += 1
            bb += score[p]
            aa = max(aa, bb)
            p += 1
            if p == len(q):
              p = 0
        A[i] = aa            
      else:
        ll = int(K / len(q)) 
        rr = K % len(q)
        aa = -float("inf")
        for j in range(len(q)):
          time = 0
          bb = ll * roop
          p = j
          while time != len(q):
            time += 1
            bb += score[p]
            if time == rr + 1:
              bb -= roop
            aa = max(aa, bb)
            p += 1
            if p == len(q):
              p = 0
        A[i] = aa           
        

#print(A)      
print(max(A))      
      
      
    
    
    
