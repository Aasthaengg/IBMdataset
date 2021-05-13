faces = input().split()

q = int(input())

for i in range(q):
    
    s = input().split()
    
    ss = s[0] + s[1]
    
    if ss in (faces[1] + faces[2] + faces[4] + faces[3] + faces[1]):
        # 1
        print(faces[0])
        
    elif ss in (faces[0] + faces[3] + faces[5] + faces[2] + faces[0]):
        # 2
        print(faces[1])
        
    elif ss in (faces[0] + faces[1] + faces[5] + faces[4] + faces[0]):
        # 3
        print(faces[2])
        
    elif ss in (faces[0] + faces[4] + faces[5] + faces[1] + faces[0]):
        # 4
        print(faces[3])
        
    elif ss in (faces[0] + faces[2] + faces[5] + faces[3] + faces[0]):
        # 5
        print(faces[4])
        
    elif ss in (faces[1] + faces[3] + faces[4] + faces[2] + faces[1]):
        # 6
        print(faces[5])
        
    else:
        print('error', ss)


