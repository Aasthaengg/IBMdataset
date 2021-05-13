n = int(input())
pages = 0
if n%2 == 1:
    pages += 1
pages += n//2
print(pages)