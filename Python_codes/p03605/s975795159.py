arr = map(int, raw_input())
n = len(arr)

for i in range(n):
    if arr[i] == 9 or arr[i-1] == 9:
        print "Yes"
        break
    else:
        print "No"
        break
