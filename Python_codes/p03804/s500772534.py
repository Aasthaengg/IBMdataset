n, m = map(int, input().split())
an = [input() for _ in range(n)]
bm = [input() for _ in range(m)]

for i in range(n-m+1) :
    for j in range(n-m+1) :
      match = True
      for k in range(m) :
        for l in range(m) :
          if an[i+k][j+l] != bm[k][l] :
            match = False
            break
          else :
            continue
      if match :
        print("Yes")
        exit()
                    
print("No")