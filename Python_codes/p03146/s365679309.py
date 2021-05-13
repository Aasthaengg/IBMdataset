s = int(input())
fn = [s]
while True:
   if fn[-1] % 2 == 0:
       if fn[-1]//2 in fn[:len(fn)-1]:
           print(len(fn) + 1)
           break
       else:
           fn.append(fn[-1] // 2)
   else:
        if fn[-1]*3 + 1 in fn[:len(fn)-1]:
            print(len(fn) + 1)
            break
        else:
            fn.append(fn[-1]*3 + 1)