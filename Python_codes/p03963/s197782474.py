ball,color = map(int,input().split())

total = color*((color-1)**(ball-1))
               
print(total)