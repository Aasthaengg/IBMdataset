N=int(input())

import sys

for h in range(1,3501):
    for n in range(h,3501):
        a=(h*n*N)
        b=(4*h*n-(n+h)*N)
        if b==0:
            continue

        
        #w=int(w)

        #if w<h:
        #    break

        #print(h,n,w)
        #print(a,b)
        if a%b==0:
            w = a/b
            if N*(n*w+h*w+h*n)!=4*n*w*h:
                continue
            #print(w)
            if w>0:
                w=int(w)
                print(h,n,w)
                '''

                print(4/N)
                print(1/h+1/n+1/w)
                print(a,b)
                print(a/b)
                '''
                sys.exit()
