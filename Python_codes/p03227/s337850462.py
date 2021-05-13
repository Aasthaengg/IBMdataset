import sys

st1=sys.stdin.readline()

if len(st1)==3:
    print(st1)

elif len(st1)==4:
    st2=st1[2]+st1[1]+st1[0]
    print(st2)

else:
    sys.exit(0)