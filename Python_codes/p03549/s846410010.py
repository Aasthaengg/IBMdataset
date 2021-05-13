import io

nim,mike=map(int,input().split())
print((1900*mike+100*(nim-mike))*2**mike)