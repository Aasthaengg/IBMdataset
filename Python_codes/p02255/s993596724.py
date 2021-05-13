def insertionSort(length, numbers):
     for i in range(length):
          for k in range(length):
               if numbers[i] <= numbers[k]:
                    numbers.insert(k, numbers[i])
                    del numbers[i+1]
                    print ' '.join(map(str, numbers))
                    break
          

length = int(raw_input())
numbers = map(int, raw_input().split())


insertionSort(length, numbers)