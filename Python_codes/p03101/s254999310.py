rh,rw = map(int,input().split())
ch,cw = map(int,input().split())

print(rh*rw-(rw*ch+(rh-ch)*cw))

