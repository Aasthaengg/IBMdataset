#coding:utf-8
h = 1
w = 1

while h+w != 0:
    h, w=input().rstrip().split(" ")
    h = int(h)
    w = int(w)
    if h == 0:
        if w==0:
            break
#???
    print("#"*w)
    for i in range(h-2):
        print("#" + "."*(w-2) +"#")
#???
    print("#"*w)
    print("")