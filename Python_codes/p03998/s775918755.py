class Player:
    def __init__(self,name,hands):
        self.name=name
        self.hands=hands

def discard(player):
    if len(player.hands)==0:
        return player.name
    tmp=player.hands.pop(0)
    if tmp=="a":
        return discard(A)
    if tmp=="b":
        return discard(B)
    if tmp=="c":
        return discard(C)


A=Player("A",list(input()))
B=Player("B",list(input()))
C=Player("C",list(input()))
print(discard(A))