import sys,os,platform
if __debug__ and platform.platform()=='Darwin-18.7.0-x86_64-i386-64bit' and os.name=='posix':
    sys.stdin = open('INP01.txt', 'r')  

    # Printing the Output to output.txt file 
    sys.stdout = open('out.txt', 'w') 
x=int(input()) 
print(1-x)