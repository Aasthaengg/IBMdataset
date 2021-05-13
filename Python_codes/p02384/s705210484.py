pattern = {
           "12651":3,
           "15621":4,
           "13641":5,
           "14631":2,
           "23542":1,
           "24532":6,
          }

label = input().split()
l2d = {label[i]:str(i+1) for i in range(6)}

qn = int(input())
for i in range(qn):
    top, front = input().split()
    tf = l2d[top]+l2d[front]

    for p in pattern:
        if tf in p:
            print(label[pattern[p]-1])