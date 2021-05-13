numbers=input()
slimmes=raw_input()
slimmes=slimmes.split(" ")

prev=slimmes[0]
count=0
spell=False
for i in range(1,numbers):
    if (prev==slimmes[i] and spell==False):
        count+=1
        spell=True
    else:
        spell=False
        
    prev=slimmes[i]
    
print count
