H=1
while H:
 H,W=map(int,raw_input().split());S="#"*W+"\n"
 if H:print S+("#"+"."*(W-2)+"#\n")*(H-2)+S
